import React from 'react';
import ReactDOM from 'react-dom';

const dataFromDjango = JSON.parse(document.querySelector('#team-info').textContent)
console.log("Data From Django", dataFromDjango)

class App extends React.Component {
  constructor () {
    super()
    this.teamData = dataFromDjango
  }

  render () {
    return (
      <h1>Hello, {this.teamData.team_name }</h1>

    )
  }
}
ReactDOM.render(<App />, document.getElementById('react-app'));

