import * as React from 'react'
import CommentsBlock from 'simple-react-comments'

class Comments extends React.Component {
  constructor (props) {
    super(props)
    console.log(props)
    this.commentsRef = React.createRef()
    this.state = {
      comments: [
        {
          comment_id: '1',
          comment_body: 'Hello',
          comment_user: 'username1'
        }
      ]
    }
  }

  const request = axios.create({
   
  })
  

  getPostComments ({ props }) {

  }

  componentDidMount () {

    // axios get request using that postId for the pk
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
