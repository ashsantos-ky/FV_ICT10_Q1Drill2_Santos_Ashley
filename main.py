from js import document

#to display the message
def display_info(event=None):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

#multi-line f-string 
    message = f"""
    <div class='result-title'>Student Profile</div>
    Name: {name} <br>
    Age: {age} <br>
    School: {school} <br>
    <br>
    <div class='result-title notes-title'>More Info</div>
    <span class='notes'>\t My name is{name}, I am \"{age}\" years old and I study at {school}. Thank you for getting to know me!</span>
    """

#to show the result in the output div
    result = document.getElementById("output")
    result.innerHTML = message
    result.style.display = "block"

#to connect with button and generate the message
document.getElementById("generate-btn").onclick = display_info
