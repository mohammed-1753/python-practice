def https_status(status):
    match status:
        case 200:
            return "fuck off"
        case 404:
            return "not found"
        case 753:
            return "unknown status code"

print(https_status(404))
print(https_status(200))
print(https_status(753))