import React from 'react'
import './Forms.css'

export default function RegisterPage() {
  return (
    <>
      <div className="allcontainer">
        <form>
          <h1>Register Form</h1>
            <div className="formcontainer">
              <div className="container">
                <div>
                  <input type="text" name='email' placeholder="Enter Email"/>
                </div>
                <div>
                  <input type="password" name='password1' placeholder="Enter Password"/>
                </div>
                <div>
                  <input type="password" name='password2' placeholder="Enter Password(again)"/>
                </div>
                <div>
                  <input type="text" name='first_name' placeholder="Enter First"/>
                </div>
                <div>
                  <input type="text" name='last_name' placeholder="Enter Last Name"/>
                </div>
                <div>
                  <input type="text" name='phone' placeholder="Enter Phone"/>
                </div>
                <div>
                  <input type="text" name='city' placeholder="Enter City"/>
                </div>
                <button type="submit">Register</button>
              </div>
            </div>
          </form>
      </div>
    </>
  )
}
