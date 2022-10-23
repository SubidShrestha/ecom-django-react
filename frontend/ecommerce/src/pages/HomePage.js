import React, {useEffect, useState} from 'react'
import { useParams,Link } from 'react-router-dom'
export default function HomePage() {
    
    let {page} = useParams()

    const url = page? `http://127.0.0.1:8000/api/stores/products?page=${page}` : "http://127.0.0.1:8000/api/stores/products?page=1"

    const [product, setProducts] = useState([])
    let productUrl = url

    useEffect(
        () => {
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
            getProduct()
        },[productUrl])

  return (
    <>
        {
            product.results && product.results.map(
                data => (
                    <div key = {data.id}>
                        <div>{data.name}</div>
                        <div>{data.category}</div>
                        <div>{data.price}</div>
                        <div>{data.description}</div>
                        <div><img src={data.image} alt=""/></div>
                    </div>
                )
            )
        }
    </>
  )
}
