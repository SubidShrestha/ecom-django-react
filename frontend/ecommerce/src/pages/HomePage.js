import React, {useEffect, useState} from 'react'
import ReactPaginate from 'react-paginate';
import './HomePage.css'
export default function HomePage() {

    const [product, setProducts] = useState([])
    const [pageCount, setPageCount] = useState(0);
    const [currentPage, setCurrentPage] = useState(1);
     
    let productUrl= `http://127.0.0.1:8000/api/stores/products/?page=${currentPage}`
    const handlePageChange = (event) => {
		setCurrentPage(event.selected+1);
	};

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
                setProducts(data.results)
                setPageCount(Math.ceil(data.count/3));
            }
            getProduct()

        },[productUrl])

  return (
    <>
        <div className='product_container'>
        {
            product.map(
                data => (
                    <div key = {data.id} className='product_item'>
                        <div><img src={data.image} alt="" className='image'/></div>
                        <div className='product-name'>{data.name}</div>
                        <div style={{padding: "5px"}}><label>Category:</label> {data.category}</div>
                        <div style={{padding: "5px"}}><label>Price:</label> Rs.{data.price}</div>
                        <div style={{padding: "5px"}}><label>Description:</label> {data.description}</div>
                        <button type="submit">Select Product</button>
                    </div>
                )
            )
        }
        </div>
        
        
        <ReactPaginate
        pageCount={pageCount}
		pageRange={pageCount}
		marginPagesDisplayed={pageCount}
		onPageChange={handlePageChange}
        renderOnZeroPageCount={null}
        containerClassName={"pagination"}
        previousLinkClassName={"pagination__link"}
        nextLinkClassName={"pagination__link"}
        pageLinkClassName={"pagination__link"}
        disabledClassName={"pagination__link--disabled"}
        activeClassName={"pagination__link--active"}
        />
    </>
  )
}
