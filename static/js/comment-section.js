import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'

const commentSection = document.getElementById('comment-section')
if (commentSection) {
  ReactDOM.render(<Comments />, commentSection)
}
