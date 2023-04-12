# Logo Compiler
Un interprete logo para realizar los ejercicios de la codeleathon sin ningun esfuerzo



## ¿Como quitar la etiqueta nocopy de Codelearn para poder copiar los ejercicios?
#### Pega esto en tu terminal del navegador:
```javascript
document.querySelectorAll("nocopy").forEach(node => {
  node.innerHTML = " ";
})
```