// 検証中
export type Riddle = {
  id: number
  creator: {
    id: number
    name: string
    image: string
    url: string
  }
  type_str: string
  level_str: string
  time_str: string
  name: string
  image: string
  description: string
  type: string
  rating: number
  level: number
  time: number
  sukkiri: number
  story: number
  gimmick: number
  start_date: any
  end_date: any
  url: string
  playings: number
  created_at: any
  bookmarks: any
}

export type Creator = {
  name: string
  image: string
  url: string
}
