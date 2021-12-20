from replit import clear

#grading calculator
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for thing in student_scores:
#   grade = ""
#   if student_scores[thing] > 89:
#     grade = "Fantastic"
#   elif student_scores[thing] > 79:
#     grade = "Very Good"
#   elif student_scores[thing] > 69:
#     grade = "Acceptable"
#   else:
#     grade = "Fail"
#   student_grades[thing] = grade
# print(student_grades)

#nesting lists

# bamboo_species_list = {
#   "Phylostachys nigra" : "Black bamboo",
#   "Dendrocalamus minor amoenus" : "Angel Mist Ghost Bamboo",
#   "Bambusa chungii" : "Blue Chungii Bamboo"
# }
# #include labels
# bamboo_information = {
#   "Bamboo Species Name" : ["Average Height", "Minimum growing zone", "Maximum growing zone", "clumping", "notes"],
#   "Bambusa chungii" : [35, 8, 11, True, "Minimum zone is 8b?"] 
# }
# #dictionaries within lists
# bamboo_dictionary_list = [
#   {
#   "species_name": "Dendrocalamus minor amoenus",
#   "average_height": 35,
#   "minimum_zone": 9,
#   "maximum_zone": 11,
#   "clumping": True,
#   "notes": "Minimum zone is 9b?"
#   }
# ]
# #dictionaries within dictionaries
# bamboo_dictionary_dictionary = {
#   "Phylostachys nigra" : {"average_height": 30, "Minimum growing zone": 7, "Maximum growing zone": 9, "clumping": False, "notes": "Shoots emerge green and turn black over years"}
#   }

#adding dictionaries to lists
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# def add_new_country(name, visit, city):
#   n = {}
#   n["country"] = name
#   n["visits"] = visit
#   n["cities"] = city
#   travel_log.append(n)
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

#Auction program
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")
bids_list = {}
top_bid = 0
def add_bids(bidder_name, bidder_bid):
  bids_list[bidder_name] =  bidder_bid
additional_bidders = "yes"
while additional_bidders == "yes":
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  add_bids(name, bid)
  additional_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()
for bid in bids_list:
  if bids_list[bid] > top_bid:
    top_bid = bids_list[bid]
winner  = bids_list[top_bid]