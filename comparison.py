import numpy as np
import pandas as pd

null = 0
json1 = {
    "_id": {
      "$oid": "632c8fda2fdd0fd7106a0d2a"
    },
    "organization": {
      "$oid": "62c27fa820f21d670b1e95d0"
    },
    "workspace": {
      "$oid": "62c27fb220f21d670b1e95d4"
    },
    "module": {
      "$oid": "62f58f68f26cc1b166cc99bf"
    },
    "submodule": {
      "$oid": "62f58fd3f26cc1b166cc99c7"
    },
    "configuration": {
      "$oid": "632c8f927f2a04c1bf9a78dc"
    },
    "token": {
      "$oid": "632bb5e33e8d86bef3f43c11"
    },
    "user": {
      "$oid": "632b30a83e8d86bef3f43bc9"
    },
    "cycle": {
      "$oid": "632b31591219cda608e7a578"
    },
    "region": {
      "$oid": "62e4216403aabb48cee3ad58"
    },
    "zone": {
      "$oid": "62e4216403aabb48cee3ad5a"
    },
    "depot": {
      "$oid": "62e4216503aabb48cee3ad5c"
    },
    "group": {
      "$oid": "62e4216503aabb48cee3ad5e"
    },
    "route": {
      "$oid": "632b30ee9f8bf04d3a86efb8"
    },
    "location": {
      "$oid": "62e2e20e633e7cd5e8fec4bf"
    },
    "status": 4,
    "process_type": 1,
    "real_date": {
      "$date": {
        "$numberLong": "1663864793000"
      }
    },
    "props": {
      "store_id": "62e2e20e633e7cd5e8fec4bf"
    },
    "data": {
      "outside_photo": {
        "image": {
          "$oid": "632c8fda2fdd0fd7106a0d2b"
        },
        "photo_types": null,
        "global_tags": 1,
        "org_tags": 0,
        "proj_tags": 0
      },
      "n_doors_ccx": 1,
      "n_doors_gepp_and_other": 1,
      "doors_ccx": [
        {
          "item": {
            "n_parrillas": 2
          },
          "photos": [
            {
              "image": {
                "$oid": "632c8fda2fdd0fd7106a0d2c"
              },
              "photo_types": {
                "door_type": "o"
              },
              "global_tags": 2,
              "org_tags": 0,
              "proj_tags": 0
            }
          ]
        }
      ],
      "doors_gepp_and_others": [
        {
          "item": {
            "n_parrillas": 3
          },
          "photos": [
            {
              "image": {
                "$oid": "632c8fda2fdd0fd7106a0d2d"
              },
              "photo_types": {
                "door_type": "c"
              }
            }
          ]
        }
      ],
      "isotonicos": 0,
      "agua_embotellada": 0,
      "garrafon_existance": 1,
      "garrafon": {
        "image": null,
        "photo_types": null,
        "global_tags": 4,
        "org_tags": 0,
        "proj_tags": 0
      },
      "jugos_existance": 1,
      "alcohol_existance": 1,
      "alcohol": {
        "image": null,
        "photo_types": null
      },
      "leche_existance": 1,
      "leche": {
        "image": null,
        "photo_types": null
      },
      "helado_existance": 1,
      "helado": {
        "image": null,
        "photo_types": null
      },
      "sabor_ccx": 150,
      "sabor_other": 250,
      "sale_ccx": 250,
      "ccx_boxes": {
        "image": null,
        "photo_types": null
      },
      "sale_other": 350,
      "other_boxes": {
        "image": null,
        "photo_types": null
      }
    },
    "date": {
      "$date": {
        "$numberLong": "1663864794455"
      }
    }
  }




def comparison():
    for i in range(0,1):
        print(json1)
    return
# Returns the key values from the list
# Important in order to start comparing between json's
# print(sorted(json1))

# List our json object
json1_list = sorted(json1.items())
# print(pd.DataFrame(json1_list))

json1_list_df = pd.DataFrame(json1_list, columns = ['key','values']).iloc[3]


print(pd.DataFrame(sorted(json1_list_df.items())).loc(3))