import math


def solution(fees, records):

    parking_record = {}
    parking_time = {}
    parking_lot = set()
    for record in records:
        time, number, command = record.split()
        if command == 'IN':
            parking_time[number] = time_to_minute(time)
            parking_lot.add(number)
        else:
            parking_lot.remove(number)
            if number in parking_record:
                parking_record[number] += time_to_minute(time) - parking_time[number]
            else:
                parking_record[number] = time_to_minute(time) - parking_time[number]
    for number in parking_lot:
        out_time = time_to_minute('23:59')
        if number in parking_record:
            parking_record[number] += out_time - parking_time[number]
        else:
            parking_record[number] = out_time - parking_time[number]

    base_time, base_fee, time_unit, fee_unit = fees
    p_key = sorted(parking_record)
    answer = []
    for k in p_key:
        answer.append(fee_settlement(parking_record[k], base_time, base_fee, time_unit, fee_unit))
    return answer


def time_to_minute(time):
    hour, minute = time.split(":")
    return int(hour)*60+int(minute)


def fee_settlement(minute, b_time, b_fee, t_unit, f_unit):
    result = b_fee
    if minute <= b_time:
        return result
    else:
        result += f_unit*math.ceil((minute-b_time)/t_unit)
        return result


fees_example = [180, 5000, 10, 600]
records_example = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                   "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees_example, records_example))
fees_example = [120, 0, 60, 591]
records_example = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT",
                   "18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees_example, records_example))
fees_example = [1, 461, 1, 10]
records_example = ["00:00 1234 IN"]
print(solution(fees_example, records_example))