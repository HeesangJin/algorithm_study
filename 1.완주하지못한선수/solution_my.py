def solution(participant, completion):
    # make part members with count
    part_members_with_count = {}
    for person_part in participant:
        if person_part not in part_members_with_count: # add new name
            part_members_with_count[person_part] = 1
        else: # add one to the existing name
            part_members_with_count[person_part] = part_members_with_count[person_part] + 1

    # check out completion members
    # part_members_with_count - each completion member
    for person_comp in completion:
        if person_comp in part_members_with_count:
            if part_members_with_count[person_comp] > 0:
                part_members_with_count[person_comp] = part_members_with_count[person_comp]-1

    # check out the non completion member
    answer = ''
    for person in part_members_with_count:
        if part_members_with_count[person] > 0:
            answer = person

    return answer