async function fetchAllOrders() {
    try {
        const response = await fetch('orders/');
        if(!response.ok) throw new Error('fetchAllOrders: fetch failed');
        const orders = await response.json();
        return orders;
    } catch(error) {
        console.log('fetchAllOrders:', error);    
        return [];
    }
}

async function createOrder(orderData) {
    try {
        const response = await fetch(`orders/`, {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json', 
            },
            body: JSON.stringify(orderData),
        });

        if (!response.ok) throw new Error('createOrder: create failed');
        return true;

    } catch(error) {
        console.log('createOrder: ', error);
        return false;
    }
}

async function updateOrder(order_data) {
    try {
        const response = await fetch(`orders/${order_data.order_id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(order_data),
        });

        if (!response.ok) throw new Error('updateOrder: update failed');
        return true;

    } catch (error) {
        console.log('updateOrder: ', error);
        return false;
    }
}

async function deleteOrder(order_id) {
    try {
        const response = await fetch(`orders/delete/${order_id}/`, {
            method: 'DELETE'
        });
        if (response.status === 200) {
            console.log(`${idno} successfully deleted.`);
            return true;
        }
    } catch(error) {
        console.log('deleteOrder: ', error);
        return false;
    }
}