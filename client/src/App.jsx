import React, { useEffect, useState } from 'react'
import axios from 'axios'

const App = () => {

  // Fetch backend api
  const fetchAPI = async () => {
    const response = await axios.get('http://localhost:5000/users')
    console.log(response.data.users)
  }

  useEffect(() => {
    fetchAPI()
  }, [])
  
  return (
    <div>
      Hello World
    </div>
  )
}

export default App
