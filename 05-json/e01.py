import json


sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}


def roundtrip(obj):
    text = json.dumps(obj)
    return json.loads(text)



print("compact:", json.dumps(sample))


print("indented:")
print(json.dumps(sample, indent=2, sort_keys=True))


after = roundtrip(sample)

print(
    f"scores type before: {type(sample['scores']).__name__} "
    f"| after: {type(after['scores']).__name__}"
)

print(
    f"married after: {after['married']} "
    f"| nickname after: {after['nickname']}"
)

print(f"equal after round trip: {sample == after}")


print("int keys:", roundtrip({1: "a", 2: "b"}))

try:
    json.dumps({"items": {1, 2, 3}})
except TypeError as e:
    print("TypeError:", e)