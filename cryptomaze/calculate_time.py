from datetime import datetime
import datetime as dt


def calc_time(last_claim_date):
    t1 = last_claim_date.strftime('%Y,%m,%d,%H,%M,%S')
    t2 = datetime.utcnow().strftime('%Y,%m,%d,%H,%M,%S')

    t1 = t1.split(',')
    t2 = t2.split(',')

    a = dt.datetime(int(t1[0]), int(t1[1]), int(t1[2]),
                    int(t1[3]), int(t1[4]), int(t1[5]))
    b = dt.datetime(int(t2[0]), int(t2[1]), int(t2[2]),
                    int(t2[3]), int(t2[4]), int(t2[5]))

    time_count = int((b-a).total_seconds())

    return time_count
