story1 = {"start": "There once was a boy who was an orphan, raised by a pack of  Wolves.",
          "middle": "He must fight for his and his families lives as their home is threatened by raging hippos",
          "end": "The boy shows great strength and resolve earning the respect of the hippos and saving his family"}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

for key in story1:
    print(story1[key])

story1["hero"] = "Wolf Boy"
print(story1)
