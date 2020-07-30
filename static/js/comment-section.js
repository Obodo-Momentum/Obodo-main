import React from 'react'
import ReactDOM from 'react-dom'
import Comments from './components/comments'

export function getPostPk(){
    
}

const commentSection = document.getElementById('comment-section')
if (commentSection) {
  ReactDOM.render(<Comments />, commentSection)