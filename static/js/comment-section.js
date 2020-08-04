import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'
import AddComment from './components/addComment'

const commentSections = document.querySelectorAll('.commentSection')
for (const commentSection of commentSections) {
  ReactDOM.render(<Comments postId={commentSection.dataset.postId} />, commentSection)
}

function getCookie (name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
const csrftoken = getCookie('csrftoken')

const addCommentSections = document.querySelectorAll('.addCommentSection')
for (const addCommentSection of addCommentSections) {
  ReactDOM.render(<AddComment postId={addCommentSection.dataset.postId} />, addCommentSection)
}
