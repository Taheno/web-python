const btn = document.querySelectorAll('.butao')
btn[0].addEventListener('click',clicou)
btn[1].addEventListener('click', clicou)
btn[3].addEventListener('click', mudarCorFundo)


function clicou (){
alert("Você Clicou Aqui")
}

function mudarCorFundo(){

let color1 = (Math.random(255)*100).toFixed(0);
let color2 = (Math.random(255)*100).toFixed(0);
let color3 = (Math.random(255)*100).toFixed(0);

let cor = 'rgb('+ color1 +','+color2 +','+ color3 +')'

document.querySelector('body').style.backgroundColor = cor
}

function soma(num1, num2){
    const resultado = num1 + num2
    return(resultado)
}

function produto(num1, num2){
    const resultado = num1 * num2
    return(resultado)
}

function subtração(num1, num2){
    const resultado = num1 - num2
    return(resultado)
}

function divisão(num1, num2){
    const resultado = num1 / num2
    return(resultado)
}

function potenciacao(num1, num2){
    const resultado = num1 ** num2
    return(resultado)
}

function modulo(num1, num2){
    const resultado = num1 % num2
    return(resultado)
}

console.log('Soma:',soma(10,5))
console.log('Produto:',produto(10,5))
console.log('Subtração:',subtração(10,5))
console.log('Divisão:',divisão(10,5))
console.log('Potenciacao:',potenciacao(10,5))
console.log('Modulo:',modulo(10,5))




function somaCalc(){
    let num1 = parseInt(document.querySelector('#num1').value)
    let num2 = parseInt(document.querySelector('#num2').value)
    alert(`Soma: ${num1+num2}`)
}