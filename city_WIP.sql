CREATE OR REPLACE FUNCTION city(x varchar)
    returns varchar
stable
as $$
    from address import AddressParser, Address
    import re
    dist = {'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR', 'CALIFORNIA': 'CA', 'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DELAWARE': 'DE', 'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID', 'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 'MAINE': 'ME', 'MARYLAND': 'MD', 'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 'MISSISSIPPI': 'MS', 'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV', 'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY', 'NORTH CAROLINA': 'NC', 'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK', 'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC', 'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT', 'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV', 'WISCONSIN': 'WI', 'WYOMING': 'WY', 'DISTRICT OF COLUMBIA': 'DC', 'ALA.': 'AL', 'ALASKA': 'AK', 'ARIZ.': 'AZ', 'ARK.': 'AR', 'CALIF.': 'CA', 'COLO.': 'CO', 'CONN.': 'CT', 'DEL.': 'DE', 'FLA.': 'FL', 'GA.': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID', 'ILL.': 'IL', 'IND.': 'IN', 'IOWA': 'IA', 'KAN.': 'KS', 'KY.': 'KY', 'LA.': 'LA', 'MAINE': 'ME', 'MD.': 'MD', 'MASS.': 'MA', 'MICH.': 'MI', 'MINN.': 'MN', 'MISS.': 'MS', 'MO.': 'MO', 'MONT.': 'MT', 'NEB.': 'NE', 'NEV.': 'NV', 'N.H.': 'NH', 'N.J.': 'NJ', 'N.M.': 'NM', 'N.Y.': 'NY', 'N.C.': 'NC', 'N.D.': 'ND', 'OHIO': 'OH', 'OKLA.': 'OK', 'ORE.': 'OR', 'PA.': 'PA', 'R.I.': 'RI', 'S.C.': 'SC', 'S.D.': 'SD', 'TENN.': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT', 'VT.': 'VT', 'VA.': 'VA', 'WASH.': 'WA', 'W.VA.': 'WV', 'WIS.': 'WI', 'WYO.': 'WY', 'D.C.': 'DC'}
    states = list(set(dist.keys()))
    state_posts = list(set(dist.values()))
    all_states = states+state_posts
    try:
        ap = AddressParser()
        x = str(x)
        city = ap.parse_address(x).city
        return city.lower()
    except:
        if any(word.upper() in all_states for word in re.split(':| |,|/|-', x)):
            a = re.split(':| |,|/|-', x)
            a.reverse()
            state = next(word for word in a if word.upper() in all_states)
            words = x.replace(state, '')
        elif any(state in x.upper() for state in states):
            state = next(state for state in states if state in x.upper())
            words = x.upper().replace(state, '')
        else:
            words = x
        words = words.replace(',','').replace(':','').replace('/','').strip()
        if not(ap.parse_address(x).house_number and ap.parse_address(x).street) and len(words.strip()) < 30 and any(i.isalpha() for i in words) and words.lower() != 'none':
            return words.lower()
        return None    
$$ language plpythonu;
