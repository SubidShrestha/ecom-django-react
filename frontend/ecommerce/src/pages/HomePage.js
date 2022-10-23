import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
export default function HomePage() {
    
    const {page} = useParams()

    const [product, setProducts] = useState([])
    let productUrl = `http://127.0.0.1:8000/api/stores/products?page=${page}`

    const getProduct = async() =>{
        let response = await fetch(productUrl,
            {
                method:'GET',
                headers:{
                    'Content-Type': 'application/json',
                }
            })
        let data = await response.json()
        console.log(data);
        setProducts(data)
    }

    useEffect(
        () => {
            getProduct()
        },[]
    )

  return (
    <>
        {
            product.map(
                data => (
                    <div key = {data.id}>
                        <div>{data.name}</div>
                        <div>{data.category}</div>
                        <div>{data.price}</div>
                        <div>{data.description}</div>
                        <div><img src={`http://127.0.0.1:8000${data.image}`} alt=""/></div>
                    </div>
            )
        )
        }
    </>
  )
}
