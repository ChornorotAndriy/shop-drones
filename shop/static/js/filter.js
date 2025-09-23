// let doc = document.querySelector()
$(document).ready(function(){
    $('#filter').on('click', function(){
        $.ajax({
            contentType: 'application/json',
            url: "/shop/filter",
            type: 'post',
            data: $('#select').val(),
            success: function(response){
                // 1 
                // $('#products').html('')
                // 2
                $('#products').empty()
                // 
                for (let product of response['products']){
                    let productDiv = $('<div>', {class: 'product'})
                    productDiv.append($('<img>', {src: `/shop/static/images/products/${product.product_name}.png`, width: '300px', height: '300px'}))
                    productDiv.append($('<h1>', {text: 'Назва продукту: ' + product.product_name}))
                    $("#products").append(productDiv)
                }
                // let html = ''
                // response['products'].forEach(product => {
                //     html += `
                //         <div class = 'product'>
                //             <hr>
                //             <img src="/shop/static/images/products/${product.product_name }.png" alt="${product.product_name}" width="300px" height="300px">
                //             <h4>Назва продукту: ${product.product_name}</h4>
                //         </div>
                //     ` 
                // });
                // $('#products').html(html)
            }
        })
    })
})