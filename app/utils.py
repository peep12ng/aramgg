def version_to_id(version):
    return "".join([version.split(".")[0], version.split(".")[1], "01"])

def match_version_to_version(version):
    return "".join([version.split(".")[0], ".", version.split(".")[1], ".1"])