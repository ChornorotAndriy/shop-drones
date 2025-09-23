import Project

def main(): 
    try:
        Project.load_env()
        Project.project.run(debug= True, port= 8001)
    except Exception as error:
        print(error)
        
if __name__ == '__main__':
    main() 