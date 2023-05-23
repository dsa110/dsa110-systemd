from dsautils import dsa_store
from astropy.time import Time
from time import sleep
import os

ds = dsa_store.DsaStore()
thresh = 10
wait = 9
longwait = 200

print('Starting antmc monitoring loop')
while True:
    dts = []
    for i in range(1, 117):
        try:
            dts.append(ds.get_dict(f'/mon/ant/{i}')['time'])
        except AttributeError:
            pass

    dts = sorted(dts)
    dt0 = 24*3600*(Time.now().mjd-dts[0])
    dt4 = 24*3600*(Time.now().mjd-dts[4])
    if dt0 > thresh:
        print(f'\t Oldest ant monitor point ({dt0}) is stale. Continuing...')
        if dt4 > thresh:
            print(f'\t Five oldest ant monitor points ({dt4} are stale). Restarting antmc...')
            os.system('sudo systemctl restart antmc')
        sleep(longwait)
    sleep(wait)
