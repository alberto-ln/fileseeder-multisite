import {defineField, defineType} from 'sanity'

export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'document',
  fields: [
    defineField({
      name: 'name',
      title: 'Nombre',
      type: 'string'
    }),
    defineField({
      name: 'slug',
      type: 'slug',
      options: {
        source: 'name',
        maxLength: 96,
        isUnique: (value, context) => context.defaultIsUnique(value, context)
      }
    }),
  ],
  preview: {
    select: {
      title: 'name',
    }
  }
})