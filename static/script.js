// js

document.addEventListener('DOMContentLoaded', function() {
    const submitHelpForm = document.getElementById('submitHelp')

    console.log(submitHelpForm)
    submitHelpForm.addEventListener("click", (e)=>{
    	console.log(e)
    	getCommand(e)
    })



    })

// const toggleBtn = document.querySelector('.toggle_btn')
// const toggleBtnIcon = document.querySelector('.toggle_btn i')
// const dropDownMenu = document.querySelector('.dropdown_menu')

// toggleBtn.onclick = function (){
//     dropDownMenu.classList.toggle('open')
//     const isOpen = dropDownMenu.classList.contains('open')

//     toggleBtnIcon.classList = isOpen
//         ? 'fa-solid fa-xmark'
//         : 'fa-solid fa-bars'
// }

function commandLine(command){
    // alert(`clicked-home`)
    if(command === null){
        command = 'help'
    }



    fetch(`http://0.0.0.0:5000?command=${command}`)
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
        // display_quotes(data, url)

        return data
    })
    
}


const helpCommand = `<ul><li>help - List available commands</li><li>about - Display my bio</li><li>read - Redirect to my blog</li><li>code - Redirect to my Github</li><li>watch - Redirect to my videos</li><li>hire - Redirect to my resume</li><li>contact - Show my contacts</li></ul>`
const unknownCommandText = `<ul><li>Unknown command. Don't sweat, type 'help' to list cmd</li></ul>`
function getCommand(e){
	e.preventDefault();
	console.log(e)
	const command = document.getElementById('command').value
	const modalP = document.getElementById('commandModal')
	modalP.innerHTML =""
	if (command =="help"|| command == ""){
		modalP.innerHTML = helpCommand
	}
	else if (command == "code"){
		window.open('https://github.com/652-Animashaun', '_blank').focus();
	}
	else if (command == "cv"){
		window.open('https://docs.google.com/document/d/1UaL_FxfmxVfMiif2Q-CLepKQLI3rm61_eLT6ohaAzhs/edit?usp=sharing', '_blank').focus();
	}
	else if (command == "about"){
		window.open('https://github.com/652-Animashaun/hello-world', '_blank').focus();
	}
	
	else if (command == "contact"){
		window.open('https://www.linkedin.com/in/mu-izz-animashaun-8682b091/', '_blank').focus();
	}
	else if (command == "hire"){
		window.open('https://docs.google.com/document/d/1UaL_FxfmxVfMiif2Q-CLepKQLI3rm61_eLT6ohaAzhs/edit?usp=sharing', '_blank').focus();
	}
	
	else if (command == "watch"){
		window.open('https://www.youtube.com/channel/UCJeiqjQxTC9Uq9scEM7VDxQ', '_blank').focus();
	}
	else{

		modalP.innerHTML = unknownCommandText
	}

}
