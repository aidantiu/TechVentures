import React, { useEffect, useState } from 'react'
import axios from 'axios'

const App = () => {

  const [array, setArray] = useState([])

  // Fetch backend api
  const fetchAPI = async () => {
    const response = await axios.get('http://localhost:5000/users')
    console.log(response.data.users)
    setArray(response.data.users)
  }

  // Fetch API on component mount
  useEffect(() => {
    fetchAPI()
  }, [])
  
  return (
    <div>
      {array.map((user, index) => (
        <div key={index}>
          <h1>{user}</h1>
        </div>
      ))}
    </div>
  )
}

export default App
