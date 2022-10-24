import React from 'react';
import './Forms.css';

export default function LoginPage() {
  return (
    <>
      <div class="allcontainer">
        <form>
          <h1>Login Form</h1>
            <div class="formcontainer">
              <div className='container'>
                <div>
                  <input type="text" name='email' placeholder="Enter Email"/>
                </div>
                <div>
                  <input type="password" name='password' placeholder="Enter Password"/>
                </div>
                <div>
                  <button type="Submit">Sign In</button>
                </div>
              </div>
            </div>
          </form>
      </div>
    </>
  )
}
