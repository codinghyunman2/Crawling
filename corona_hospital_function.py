def extract_info(hospital_table):
  result = []
  for hospital in hospital_table:
    info = hospital.contents

    hospital_info = {
      'city' : info[1].string,
      'city_detail' : info[2].string,
      'name' : info[3].text,
      'phone' : info[4].string
    }

    result.append(hospital_info)
  return result