from oblasti import oblasti
from narodnosti import narodnosti

from queries.IrokInarCR import IrokInarCR 
from queries.IrokInarKraj import IrokInarKraj 
from queries.IrokInarOkres import IrokInarOkres 
from queries.IrokXnarCR import IrokXnarCR 
from queries.IrokXnarKraj import IrokXnarKraj 
from queries.IrokXnarOkres import IrokXnarOkres 
from queries.XrokInarCR import XrokInarCR 
from queries.XrokInarKraj import XrokInarKraj 
from queries.XrokInarOkres import XrokInarOkres 
from queries.XrokXnarCR import XrokXnarCR 
from queries.XrokXnarKraj import XrokXnarKraj 
from queries.XrokXnarOkres import XrokXnarOkres



def getData(data, cur):
    params = data["parameters"]

    # JEDEN ROK
    if params["start_year"] == params["end_year"]:
        if params["obcanstvi_kod"] == "0":
            # VSECHNY NARODNOSTI
            if params["area_kod"] == "19":
                IrokXnarCR(data, cur)
            elif len(params["area_kod"]) == 4:
                # kraj
                IrokXnarKraj(data, cur)
            else:
                # okres
                IrokXnarOkres(data, cur)

        else:
            # JEDNA NARODNOST
            if params["area_kod"] == "19":
                # CR
                IrokInarCR(data, cur)
            elif len(params["area_kod"]) == 4:
                # kraj
                IrokInarKraj(data, cur)
            else:
                # okres
                IrokInarOkres(data, cur)

    # VICE LET
    else:
        if params["obcanstvi_kod"] == "0":
            # VSECHNY NARODNOSTI
            if params["area_kod"] == "19":
                # CR
                print(1)
                XrokXnarCR(data, cur)
            elif len(params["area_kod"]) == 4:
                # kraj
                print(2)
                XrokXnarKraj(data, cur)
            else:
                # okres
                print(3)
                XrokXnarOkres(data, cur)

        else:
            # JEDNA NARODNOST
            if params["area_kod"] == "19":
                # CR
                print(4)
                XrokInarCR(data, cur)
            elif len(params["area_kod"]) == 4:
                # kraj
                print(5)
                XrokInarKraj(data, cur)
            else:
                # okres
                print(6)
                XrokInarOkres(data, cur)


