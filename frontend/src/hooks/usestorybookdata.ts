import { useState, useEffect } from "react";
import axios from "axios";
import { StoryBook } from "../types/storybooktypes";

interface useStoryBookDataResult {
  isLoading: boolean;
  storyBookData: StoryBook | null;
}

export function useStoryBookData(storyBookId: string | undefined): useStoryBookDataResult {
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [storyBookData, setStoryBookData] = useState<StoryBook | null>(null);

  useEffect(() => {
    setIsLoading(true);
    if (storyBookId) {
      axios
        .get<StoryBook>(`${import.meta.env.VITE_APP_API_URL}/storybook/${storyBookId}`)
        .then((res) => {
          console.log(`fetch complete storybook ${storyBookId}`);
          setStoryBookData(res.data);
          setIsLoading(false);
        })
        .catch((e) => {
          console.error(`error detect ${e}`);
          setIsLoading(false);
        });
    }
  }, [storyBookId]);

  return { isLoading, storyBookData };
}
