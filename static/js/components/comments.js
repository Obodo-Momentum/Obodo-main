import React from 'react'
import axios from 'axios'
import Comment from './comment'
import AddComment from './addComment'

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
        // console.log(response.data)
        this.setState({ comments: response.data })
        // console.log(this.state.comments)
      })
  }

  render () {
    console.log(this.state.comments)
    return (
      <div>
        <div>
          {this.state.comments.map(comment => {
            return (
              <Comment comment={comment} key={comment.id} />
            )
          })}
        </div>
        <div>
          <AddComment postId={this.props.postId} />
        </div>
      </div>
    )
  }
}

export default Comments
