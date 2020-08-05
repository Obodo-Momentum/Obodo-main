import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'

const commentSections = document.querySelectorAll('.commentSection')
for (const commentSection of commentSections) {
  ReactDOM.render(<Comments postId={commentSection.dataset.postId} />, commentSection)
}
