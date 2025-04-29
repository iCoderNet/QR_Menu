function plusOrderProduct(currentTarget) {
    // Find the closest parent with class 'product-content'
    const productContent = currentTarget.closest('.product-content');    

    if (productContent) {
        // Find the inner div with 'd-none'
        const hiddenDiv = productContent.querySelector('.d-none');

        if (hiddenDiv) {
            hiddenDiv.classList.remove('d-none');
            hiddenDiv.classList.add('d-flex');
        } else {
            const inputEL = productContent.querySelector('input[type="number"]');
            const maxNumber = Number(inputEL.getAttribute('max')) || 5;
            if (Number(inputEL.value) < maxNumber) {
                inputEL.value = Number(inputEL.value) + 1;
            }
        }
    } else {
        console.error('No .product-content ancestor found.');
    }
}

function minusOrderProduct(currentTarget) {
    // Find the closest parent with class 'product-content'
    const productContent = currentTarget.closest('.product-content');

    if (productContent) {
        // Find the inner div with 'd-none'
        const hiddenDiv = productContent.querySelector('.d-flex');

        const inputEL = productContent.querySelector('input[type="number"]');
        const minNumber = Number(inputEL.getAttribute('min')) || 1;
        if (Number(inputEL.value) > minNumber) {
            inputEL.value = Number(inputEL.value) - 1;
        }else if(Number(inputEL.value) == minNumber){
            hiddenDiv.classList.remove('d-flex');
            hiddenDiv.classList.add('d-none');
        }
    } else {
        console.error('No .product-content ancestor found.');
    }
}
