import React from 'react'
import ReactDOM from 'react-dom'
import Preview from './components/Preview'

function getDataFromForm (form) {
  const formData = new FormData(form)
  const fields = {}
  for (const key of formData.keys()) {
    fields[key] = formData.get(key)
  }
  return fields
}

const preview = document.('preview')
if (preview) {
  const postForm = document.getElementById('post-form')
  postForm.addEventListener('input', function (event) {
    const fields = getDataFromForm(postForm)
    ReactDOM.render(<Preview {...fields} />, preview)
  })
}
