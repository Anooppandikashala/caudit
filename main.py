awsServices = ["s3", "ec2"]
azureServices = ["blob", "collectors"]
gcpServices = ["disk", "compute", "policies"]
availableAuditCloudServices: dict = {"aws": awsServices, "azure": azureServices, "gcp": gcpServices}


def printHead():
    print("*" * 50)
    print("Welcome to CloudAudit")
    print("*" * 50)


def printMainMenuAndGetTheResponse():
    print("Select the Audit: ")
    menuNo = 1
    availableAuditCloudServicesList = [x for x in availableAuditCloudServices.keys()]
    for service in availableAuditCloudServicesList:
        ret = str(menuNo) + ".  " + str(service).upper()
        print(ret)
        menuNo = menuNo + 1
    response = input("Your choice:")
    # print(response)
    if response.isdigit():
        res = int(response)
        if 0 < res <= len(availableAuditCloudServicesList):
            # print(availableAuditCloudServicesList[res-1])
            return availableAuditCloudServicesList[res - 1]

    print("Invalid selection try again")
    return printMainMenuAndGetTheResponse()


def printSecondaryMenu(menuList: list):
    menuNo = 1
    for item in menuList:
        ret = str(menuNo) + ".  " + str(item).upper()
        print(ret)
        menuNo = menuNo + 1
    response = input("Your choice:")
    if response.isdigit():
        res = int(response)
        if 0 < res <= len(menuList):
            return menuList[res - 1]

    print("Invalid selection try again")
    return printSecondaryMenu(menuList)


def addKeyToDatabase(keyPath):
    # Do your code here
    pass


def getKeyFilePath():
    defaultKeyPath = "/Modules/Database/"
    path = input("Enter the key-file full path")
    if str(path).lower() != defaultKeyPath.lower() and defaultKeyPath.lower() not in str(path).lower() and str(
            path).lower() not in defaultKeyPath.lower():
        res = input("Do you want to add the key to the database? (y/n)")
        if str(res).lower() == "y":
            addKeyToDatabase(path)
    return path


def doAWSService(selectedServiceInstance):
    if selectedServiceInstance.lower() == "s3":
        print("Doing AWS S3 Audit.....!")
        # Do your code here
    elif selectedServiceInstance.lower() == "ec2":
        print("Doing AWS EC2 Audit.....!")
        # Do your code here


def doAzureService(selectedServiceInstance):
    if selectedServiceInstance.lower() == "blob":
        print("Doing Azure Blob Audit.....!")
        # Do your code here
    elif selectedServiceInstance.lower() == "collectors":
        print("Doing Azure Collectors Audit.....!")
        # Do your code here


def doGCPService(selectedServiceInstance):
    if selectedServiceInstance.lower() == "disk":
        print("Doing GCP Disk Audit.....!")
        # Do your code here
    elif selectedServiceInstance.lower() == "compute":
        print("Doing GCP Compute Audit.....!")
        # Do your code here
    elif selectedServiceInstance.lower() == "policies":
        print("Doing GCP Policies Audit.....!")
        # Do your code here


def doAudit(selectedServiceInstance: str):
    if selectedServiceInstance.lower() in awsServices:
        doAWSService(selectedServiceInstance)
    elif selectedServiceInstance.lower() in azureServices:
        doAzureService(selectedServiceInstance)
    elif selectedServiceInstance.lower() in gcpServices:
        doGCPService(selectedServiceInstance)


def startCloudAudit():
    printHead()
    selectedService = printMainMenuAndGetTheResponse()
    print(selectedService)
    secondaryMenuList = availableAuditCloudServices[selectedService]
    selectedServiceInstance = printSecondaryMenu(secondaryMenuList)
    print("Selected Service Instance: " + selectedServiceInstance)
    keyFilePath = getKeyFilePath()
    print("Key File Path" + keyFilePath)
    doAudit(selectedServiceInstance)


def start():
    while True:
        startCloudAudit()
        res = input("Do you want to audit more services? (y/n)")
        if str(res).lower() == "n":
            break


if __name__ == '__main__':
    start()
