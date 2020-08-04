import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'
import AddComment from './components/addComment'

const commentSections = document.querySelectorAll('.commentSection')
for (const commentSection of commentSections) {
  ReactDOM.render(<Comments postId={commentSection.dataset.postId} />, commentSection)
}

const addCommentSections = document.querySelectorAll('.addCommentSection')
for (const addCommentSection of addCommentSections) {
  ReactDOM.render(<AddComment postId={addCommentSection.dataset.postId} />, addCommentSection)
}
