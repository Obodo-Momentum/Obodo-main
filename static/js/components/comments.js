import * as React from 'react'
import CommentsBlock from 'simple-react-comments'
import axios from 'axios'

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
      })
  }

  componentDidUpdate () {

  }

  render () {
    return (
      <div id='comments-component' ref={this.commentsRef}>
        <CommentsBlock
          comments={this.state.comments}
          signinUrl='/signin'
          isLoggedIn
          reactRouter
          onSubmit={text => {
            if (text.length > 0) {
              this.setState({
                comments: [
                  ...this.state.comments,
                  {
                    authorUrl: '#',
                    avatarUrl: '#avatarUrl',
                    createdAt: new Date(),
                    fullName: 'Name',
                    text
                  }
                ]
              })
              console.log('submit:', text)
            }
          }}
        />
      </div>
    )
  }
}

export default Comments
