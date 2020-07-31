import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'
import axios from 'axios'

const commentSections = document.querySelectorAll('.commentSection')
console.log('comment section')
for (const commentSection of commentSections) {
  console.log('js is running')
  ReactDOM.render(<Comments postId={commentSection.dataset.postId} />, commentSection)
}
