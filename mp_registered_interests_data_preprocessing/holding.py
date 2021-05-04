reformattedJSONfiles = os.listdir("./regInterestsJsonRefactored/")
datesAndNamesTally = {}

for JSONfile in reformattedJSONfiles:
    print(f"in {JSONfile}")
    with open(f'./regInterestsJsonRefactored/{JSONfile}') as json_file: 
        fileData = json.load(json_file) 
        membersInTally = list(datesAndNamesTally.keys())
        fileMembers = list(fileData.keys())
        date = JSONfile.split(".")[0]


        for member in fileMembers:
            categoriesForSingleFile = list(fileData[member][date].keys())

            if member not in membersInTally:
                datesAndNamesTally[member] = {"datesSummary": [], "categorySummary": categoriesForSingleFile}
                datesAndNamesTally[member]["datesSummary"].append(date)
            if member in membersInTally:
                category_list_1 = categoriesForSingleFile
                category_list_2 = datesAndNamesTally[member]["categorySummary"]
                category_set_1 = set(category_list_1)
                category_set_2 = set(category_list_2)
                category_list_2_items_not_in_category_list_1 = list(category_set_2 - category_set_1)
                combined_category_list = category_list_1 + category_list_2_items_not_in_category_list_1
                datesAndNamesTally[member]["categorySummary"] = combined_category_list
                datesAndNamesTally[member]["datesSummary"].append(date)
    print(f"finished with {JSONfile}")

masterArray = []

for key in datesAndNamesTally:
    newArr = []
    for date in datesAndNamesTally[key]["datesSummary"]:
        newDate = date[0:4]
        newArr.append(newDate)
    datesAndNamesTally[key]["datesSummary"] = list(set(newArr))


#! reduce to just the years and only single years - map through removing all but year then make a set then save

with open(f"./datesAndNamesTally.JSON", "w") as entireJSON:
    json.dump(datesAndNamesTally, entireJSON)