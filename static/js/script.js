const divFileName = document.getElementById('div-filename')
const linkBack = document.getElementById('link-back')
const icon = document.getElementById('icon')
const h1TitleReport = document.getElementById('title-report')

const requestReport = async () => {

    const fetchSettings = {
        method : 'POST',
        body: JSON.stringify({fileName: divFileName.dataset.fileName}),
        headers: {"content-type": "application/json; charset=UTF-8"}
    }

    try{
        const request = await fetch('/generate_html_report', fetchSettings)
        const result = await request.json()
        return result
    }catch(error){
        return error
    }
}

requestReport().then(result => {
    if(result.code_response === 400){
        icon.classList.add('hide')
        linkBack.classList.remove('hide')
        h1TitleReport.textContent = 'The report was successfuly generated!!!'
        h1TitleReport.style.color = '#3EC70B'
        console.log('The report was successfuly generated and the code response received is:')
        console.log(result.code_response)
    }else{
        console.log('Upss we got the next error')
        console.log(result)
    }
})

