import React from 'react'
import axios from 'axios'
import Card from 'react-bootstrap/Card'

class Comments extends React.Component {
  constructor (props) {
    super(props)
    console.log(props.postId)
    this.state = {
      comments: []
    }
  }

  componentDidMount () {
    const postId = this.props.postId
    axios.get(`/api/post_comments/${postId}/`)
      .then((response) => {
        console.log(response.data)
        this.setState({ comments: response.data })
        console.log(this.comments)
      })
  }

  render () {
    return (
      <div>
        <Card></Card.Body>
        </Card>
      </div>
    )
  }
}

export default Comments
