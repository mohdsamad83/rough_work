from jinja2 import Template

data1 = [['Samad',999],['Ibrahim',789],['Surya',909]]
def main():
    with open('jinja.html','r') as file1:
        content = file1.read()
    
    value = Template(content).render(data = data1)

    with open('generator.html','w') as file2:
        file2.write(value)

    print("code generated successfully please check ")

if __name__ == "__main__":
    main()