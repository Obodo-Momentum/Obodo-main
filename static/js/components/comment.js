import React from 'react'
import Card from 'react-bootstrap/Card'

export default function Comment ({ comment }) {
  console.log({ comment })
  return (
    <Card>
      <Card.Text>{comment.comment_text}</Card.Text>
      <Card.Subtitle className=' mb-2 text-muted'>{comment.posted_at}</Card.Subtitle>
    </Card>
  )
}
