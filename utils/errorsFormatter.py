def modify_serialize_errors(err):
    error = ''
    for section, message in err.items():
        for string in message:
            error += f"{section}: {string} "


    return error
