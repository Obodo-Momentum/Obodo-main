import React from 'react'
import ReactDOM from 'react-dom'
import './add-request-or-offer'
import './comment-section'

class App extends React.Component {
  render () {
    return (
      <h1>Hello, world!</h1>
    )
  }
}

const reactApp = document.getElementById('react-app')
if (reactApp) {
  ReactDOM.render(<App />, reactApp)
}
