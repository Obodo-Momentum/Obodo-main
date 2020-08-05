import React from 'react'
import axios from 'axios'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

class AddComment extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      comment_text: '',
      posted: false
    }
    this.handleTextChange = this.handleTextChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleTextChange (event) {
    this.setState({ comment_text: event.target.value })
  }

  handleSubmit (event) {
    event.preventDefault()
    axios
      .post(`/api/post_comments/${this.props.postId}/`, {
        withCredentials: true,
        comment_text: this.state.comment_text
      })
      .then(response =>
        console.log(this.state.comment_text))
  }

  postComment (prevState) {
    if (this.state.comment_text !== prevState) { this.setState({ posted: true }) }
  }

  render () {
    return (
      <div>
        <Form onSubmit={this.handleSubmit}>
          <Form.Group controlId='formAddText'>
            <Form.Control as='textarea' rows='3' placeholder='Add a comment' value={this.state.comment_text} onChange={this.handleTextChange} />
          </Form.Group>

          <Button className='btn' type='submit' name='submit' value='submit'>
           Submit
          </Button>
        </Form>
      </div>
    )
  }
}
export default AddComment
