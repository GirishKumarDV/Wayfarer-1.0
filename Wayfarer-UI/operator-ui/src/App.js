
import './App.css';
import logo from './logo.svg'
import React from 'react';


// class connectionExample extends React.Component{
//   componentDidMount(){
//     const apiUrl = 'http://localhost:8000/operator/api'
//     fetch(apiUrl).then((response)=> response.json())
//     .then((data)=>console.log(data));
//   }
//   render(){
//     return <div>Example Connection</div>;
//   }
// }

// export default connectionExample;

function App() {
  return (
    <>
    <h1>this is react</h1>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
    </>
  );
}

export default App;
