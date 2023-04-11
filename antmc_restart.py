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

    dt = 24*3600*(Time.now().mjd-min(dts))
    if dt > thresh:
        print(f'\tStale ant monitor points ({dt}). Restarting antmc...')
        os.system('sudo systemctl restart antmc')
        print('*', end='')
        sleep(longwait)
    print('.', end='')
    sleep(wait)
