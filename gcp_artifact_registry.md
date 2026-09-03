# GCP Artifact Registry Findings

## Summary

The App Engine Standard deployment creates a container image in Artifact Registry automatically. The image is required by App Engine and should not be deleted while it is the current deployed version.

The image size is mostly Google\'s managed runtime, not the application source. The application payload is approximately 41 MB, while the pulled image reports approximately 539 MiB locally and the Artifact Registry console showed a virtual size of approximately 539 MB.

## Image investigation

The image metadata identified these managed components:

- App Engine Standard Python 3.14 runtime
- Ubuntu 24.04 based `google-24-full` stack
- Google buildpacks for Python, pip, App Engine, and runtime linking
- Google process components such as `app-runner` and `pid1`

Inside the pulled image:

```text
/usr       1.1 GB expanded
/opt       341 MB expanded
/workspace  41 MB expanded
```

The largest `/usr/lib` areas were:

```text
/usr/lib/x86_64-linux-gnu  554 MB
/usr/lib/locale             238 MB
```

Large libraries included LLVM, Gallium, ICU, Ghostscript, FFmpeg, and codec libraries. These belong to the managed Google runtime and cannot be safely removed from an App Engine Standard image.

The `du` output reports the expanded filesystem. It is not directly equivalent to Artifact Registry billable storage, because container layers are compressed and can be shared between image versions.

## Repository optimizations

The original SQLite database contained both `zaznam` and `zaznam_denormalised`, each with 919,995 rows. The application queries only `zaznam_denormalised`.

The following changes were tested and applied:

- Removed pandas from the active query engine and replaced its two small pivot operations with standard Python.
- Removed pandas from `requirements.txt`, eliminating NumPy and reducing the measured virtual-environment `site-packages` footprint from approximately 104 MB to 4.2 MB.
- Removed three indexes that SQLite did not select for representative application query plans:
  - `idx_kraj_kod`
  - `idx_rok_obcanstvi`
  - `idx_rok_vek`
- Rebuilt `separate.db.gz` with the denormalised table and the remaining nine indexes.
- The optimized uncompressed database is approximately 221.6 MiB, compared with approximately 273.5 MiB for the original database.
- The compressed database is approximately 40 MB. Pre-compressing it reduced the deployed image by approximately 23 MB, from about 608 MB to 585 MB.
- Removing pandas and indexes reduced the image by a further approximately 46 MB, from about 585 MB to 539 MB.

The API was tested successfully in a fresh environment without pandas, using the compressed database fallback. The original local `cizinci.db` remains available for development, while `.gcloudignore` excludes it from the GCP upload.

## Database startup behavior

When `cizinci.db` exists locally, the application uses it directly. In App Engine, `.gcloudignore` excludes that file, so the application imports `separate.db.gz`, decompresses it once to `/tmp/cizinci.db` during startup, and then queries the unpacked SQLite database.

The decompressed database is runtime storage on the App Engine instance. It is not part of the Artifact Registry image. Each new or restarted instance performs the extraction once.

## Artifact Registry cleanup

Old App Engine image versions remain in Artifact Registry after deployment. A cleanup policy is useful because repeated deployments otherwise accumulate old images and can exceed the free storage allowance.

The cleanup policy should retain the current image and remove old generated artifacts. Keeping only the newest image reduces storage, but also reduces rollback options.

Cleanup cannot reduce the size of the current image. It only controls accumulated historical images.

## Final conclusion

The repository-level optimizations are complete, but the remaining approximately 539 MB image is dominated by the App Engine Standard managed runtime. There is no practical source-level cleanup that will remove the large system libraries shown above.

The deployment is being moved to Cloud Run with a custom `python:3.14-slim` Dockerfile. A local build produced an approximately 90 MB image, compared with approximately 539 MiB for the App Engine Standard image. Cloud Run still uses Artifact Registry, but the custom base image avoids the large managed App Engine runtime. The Cloud Run service should remain configured with zero minimum instances so it can scale to zero when unused.

The Cloud Run service and its image repository are configured for `europe-west1`. The Artifact Registry repository must exist there before the first deployment; repository locations cannot be changed after creation. Create it once with:

```powershell
gcloud artifacts repositories create gae-standard `
  --repository-format=docker `
  --location=europe-west1 `
  --project=fourth-buffer-424217-j3
```

The GitHub deployment service account also needs Artifact Registry Writer access to this repository.
